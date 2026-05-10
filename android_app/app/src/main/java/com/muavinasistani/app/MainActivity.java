package com.muavinasistani.app;

import android.Manifest;
import android.app.Activity;
import android.content.Intent;
import android.content.ActivityNotFoundException;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.Bundle;
import android.print.PrintManager;
import android.print.PrintDocumentAdapter;
import android.print.PrintAttributes;
import android.os.Environment;
import android.os.Handler;
import android.os.Looper;
import android.provider.MediaStore;
import android.speech.RecognitionListener;
import android.speech.RecognizerIntent;
import android.speech.SpeechRecognizer;
import android.speech.tts.TextToSpeech;
import android.webkit.GeolocationPermissions;
import android.webkit.JavascriptInterface;
import android.webkit.PermissionRequest;
import android.webkit.ValueCallback;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceError;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;

import androidx.core.content.FileProvider;

import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Locale;

public class MainActivity extends Activity {
    private WebView webView;
    private boolean pageLoaded = false;

    private static final int FILE_CHOOSER_REQUEST = 501;
    private ValueCallback<Uri[]> filePathCallback;
    private Uri cameraImageUri;

    private TextToSpeech tts;
    private boolean ttsReady = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        requestBasicPermissions();

        webView = new WebView(this);
        setContentView(webView);

        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setDatabaseEnabled(true);
        settings.setAllowFileAccess(true);
        settings.setAllowContentAccess(true);
        settings.setMediaPlaybackRequiresUserGesture(false);
        settings.setLoadWithOverviewMode(true);
        settings.setUseWideViewPort(true);
        settings.setGeolocationEnabled(true);
        settings.setJavaScriptCanOpenWindowsAutomatically(true);

        tts = new TextToSpeech(this, status -> {
            if (status == TextToSpeech.SUCCESS) {
                tts.setLanguage(new Locale("tr", "TR"));
                tts.setSpeechRate(0.95f);
                tts.setPitch(1.0f);
                ttsReady = true;
            }
        });

        webView.addJavascriptInterface(new VoiceBridge(), "AndroidVoice");
        webView.addJavascriptInterface(new TtsBridge(), "AndroidTTS");

        webView.setWebChromeClient(new WebChromeClient() {
            @Override
            public void onPermissionRequest(final PermissionRequest request) {
                runOnUiThread(() -> request.grant(request.getResources()));
            }

            @Override
            public void onGeolocationPermissionsShowPrompt(String origin, GeolocationPermissions.Callback callback) {
                callback.invoke(origin, true, false);
            }

            @Override
            public boolean onShowFileChooser(
                    WebView webView,
                    ValueCallback<Uri[]> filePathCallback,
                    FileChooserParams fileChooserParams
            ) {
                if (MainActivity.this.filePathCallback != null) {
                    MainActivity.this.filePathCallback.onReceiveValue(null);
                }

                MainActivity.this.filePathCallback = filePathCallback;

                Intent cameraIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                if (cameraIntent.resolveActivity(getPackageManager()) != null) {
                    try {
                        File photoFile = createImageFile();
                        cameraImageUri = FileProvider.getUriForFile(
                                MainActivity.this,
                                "com.muavinasistani.app.fileprovider",
                                photoFile
                        );
                        cameraIntent.putExtra(MediaStore.EXTRA_OUTPUT, cameraImageUri);
                        cameraIntent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
                        cameraIntent.addFlags(Intent.FLAG_GRANT_WRITE_URI_PERMISSION);
                    } catch (IOException e) {
                        cameraIntent = null;
                    }
                }

                Intent contentIntent = new Intent(Intent.ACTION_GET_CONTENT);
                contentIntent.addCategory(Intent.CATEGORY_OPENABLE);
                contentIntent.setType("image/*");

                Intent[] intentArray = cameraIntent != null ? new Intent[]{cameraIntent} : new Intent[0];

                Intent chooserIntent = new Intent(Intent.ACTION_CHOOSER);
                chooserIntent.putExtra(Intent.EXTRA_INTENT, contentIntent);
                chooserIntent.putExtra(Intent.EXTRA_TITLE, "Fotoğraf seç veya çek");
                chooserIntent.putExtra(Intent.EXTRA_INITIAL_INTENTS, intentArray);

                startActivityForResult(chooserIntent, FILE_CHOOSER_REQUEST);
                return true;
            }
        });

        webView.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
                Uri uri = request.getUrl();
                String scheme = uri.getScheme() != null ? uri.getScheme().toLowerCase() : "";
                String host = uri.getHost() != null ? uri.getHost().toLowerCase() : "";

                if (("http".equals(scheme) || "https".equals(scheme)) &&
                        ("127.0.0.1".equals(host) || "localhost".equals(host))) {
                    return false;
                }

                try {
                    Intent intent = new Intent(Intent.ACTION_VIEW, uri);
                    startActivity(intent);
                } catch (ActivityNotFoundException e) {
                    showError("Bu bağlantı açılamadı:\n" + uri.toString());
                }
                return true;
            }

            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                Uri uri = Uri.parse(url);
                String scheme = uri.getScheme() != null ? uri.getScheme().toLowerCase() : "";
                String host = uri.getHost() != null ? uri.getHost().toLowerCase() : "";

                if (("http".equals(scheme) || "https".equals(scheme)) &&
                        ("127.0.0.1".equals(host) || "localhost".equals(host))) {
                    return false;
                }

                try {
                    Intent intent = new Intent(Intent.ACTION_VIEW, uri);
                    startActivity(intent);
                } catch (ActivityNotFoundException e) {
                    showError("Bu bağlantı açılamadı:\n" + url);
                }
                return true;
            }

            @Override
            public void onPageFinished(WebView view, String url) {
                pageLoaded = true;
                super.onPageFinished(view, url);
            }

            @Override
            public void onReceivedError(WebView view, WebResourceRequest request, WebResourceError error) {
                if (android.os.Build.VERSION.SDK_INT >= 23 && request.isForMainFrame()) {
                    showError("WebView sayfayı yükleyemedi:\n" + error.getDescription());
                }
                super.onReceivedError(view, request, error);
            }
        });

        showLoading();

        if (!Python.isStarted()) {
            try {
                Python.start(new AndroidPlatform(this));
            } catch (Exception e) {
                showError("Python başlatılamadı:\n" + e.toString());
                return;
            }
        }

        new Thread(() -> {
            try {
                Python py = Python.getInstance();
                File pyDataDir = new File(getExternalFilesDir(null), "pydata");
                if (!pyDataDir.exists()) {
                    pyDataDir.mkdirs();
                }
                py.getModule("android_server").callAttr("start_in_background", pyDataDir.getAbsolutePath());

                runOnUiThread(() -> webView.loadUrl("http://127.0.0.1:5000/"));

            } catch (Exception e) {
                showError("Flask sunucusu başlatılamadı:\n" + e.toString());
            }
        }).start();

        new Handler(Looper.getMainLooper()).postDelayed(() -> {
            if (!pageLoaded) {
                showError(
                        "Uygulama zamanında açılmadı.\n\n" +
                        "Flask sunucusu APK içinde başlamamış olabilir."
                );
            }
        }, 35000);
    }

    private File createImageFile() throws IOException {
        String timeStamp = new SimpleDateFormat("yyyyMMdd_HHmmss", Locale.US).format(new Date());
        File storageDir = getExternalFilesDir(Environment.DIRECTORY_PICTURES);
        return File.createTempFile("bagaj_" + timeStamp + "_", ".jpg", storageDir);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == FILE_CHOOSER_REQUEST) {
            Uri[] results = null;

            if (resultCode == RESULT_OK) {
                if (data == null || data.getData() == null) {
                    if (cameraImageUri != null) {
                        results = new Uri[]{cameraImageUri};
                    }
                } else {
                    results = new Uri[]{data.getData()};
                }
            }

            if (filePathCallback != null) {
                filePathCallback.onReceiveValue(results);
                filePathCallback = null;
            }

            cameraImageUri = null;
            return;
        }

        super.onActivityResult(requestCode, resultCode, data);
    }


    public class PrintBridge {
        @JavascriptInterface
        public void printPage(String jobName) {
            final String safeJobName = (jobName == null || jobName.trim().isEmpty())
                    ? "Muavin Asistani"
                    : jobName.trim();

            runOnUiThread(() -> {
                try {
                    Toast.makeText(MainActivity.this, "Yazdırma başlatılıyor...", Toast.LENGTH_SHORT).show();

                    PrintManager printManager = (PrintManager) getSystemService(PRINT_SERVICE);
                    if (printManager == null) {
                        showError("Yazdırma servisi bulunamadı.");
                        return;
                    }

                    PrintDocumentAdapter adapter = webView.createPrintDocumentAdapter(safeJobName);
                    printManager.print(
                            safeJobName,
                            adapter,
                            new PrintAttributes.Builder().build()
                    );
                } catch (Exception e) {
                    showError("Yazdırma ekranı açılamadı:\n" + e.toString());
                }
            });
        }
    }


    public class TtsBridge {
        @JavascriptInterface
        public void speak(String text) {
            final String msg = text == null ? "" : text.trim();

            if (msg.length() == 0) return;

            runOnUiThread(() -> {
                try {
                    if (tts == null) return;

                    if (!ttsReady) {
                        tts.setLanguage(new Locale("tr", "TR"));
                        ttsReady = true;
                    }

                    tts.stop();
                    tts.speak(msg, TextToSpeech.QUEUE_FLUSH, null, "muavin_tts");
                } catch (Exception ignored) {}
            });
        }

        @JavascriptInterface
        public void stop() {
            runOnUiThread(() -> {
                try {
                    if (tts != null) tts.stop();
                } catch (Exception ignored) {}
            });
        }
    }

    public class VoiceBridge {
        @JavascriptInterface
        public void startVoice() {
            runOnUiThread(() -> {
                if (!SpeechRecognizer.isRecognitionAvailable(MainActivity.this)) {
                    sendVoiceError("Android ses tanıma kullanılamıyor");
                    return;
                }

                SpeechRecognizer recognizer = SpeechRecognizer.createSpeechRecognizer(MainActivity.this);

                Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
                intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
                intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "tr-TR");
                intent.putExtra(RecognizerIntent.EXTRA_PARTIAL_RESULTS, false);
                intent.putExtra(RecognizerIntent.EXTRA_MAX_RESULTS, 1);

                recognizer.setRecognitionListener(new RecognitionListener() {
                    @Override public void onReadyForSpeech(Bundle params) {}
                    @Override public void onBeginningOfSpeech() {}
                    @Override public void onRmsChanged(float rmsdB) {}
                    @Override public void onBufferReceived(byte[] buffer) {}
                    @Override public void onEndOfSpeech() {}

                    @Override
                    public void onError(int error) {
                        sendVoiceError("Sesli komut hatası: " + error);
                        recognizer.destroy();
                    }

                    @Override
                    public void onResults(Bundle results) {
                        ArrayList<String> list = results.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION);
                        String text = (list != null && !list.isEmpty()) ? list.get(0) : "";
                        sendVoiceResult(text);
                        recognizer.destroy();
                    }

                    @Override public void onPartialResults(Bundle partialResults) {}
                    @Override public void onEvent(int eventType, Bundle params) {}
                });

                recognizer.startListening(intent);
            });
        }
    }

    private void sendVoiceResult(String text) {
        String js = "window.handleNativeVoiceResult && window.handleNativeVoiceResult(" + jsQuote(text) + ");";
        runOnUiThread(() -> webView.evaluateJavascript(js, null));
    }

    private void sendVoiceError(String text) {
        String js = "window.handleNativeVoiceError && window.handleNativeVoiceError(" + jsQuote(text) + ");";
        runOnUiThread(() -> webView.evaluateJavascript(js, null));
    }

    private String jsQuote(String s) {
        if (s == null) s = "";
        return "\"" + s
                .replace("\\", "\\\\")
                .replace("\"", "\\\"")
                .replace("\n", "\\n")
                .replace("\r", "\\r") + "\"";
    }

    private void showLoading() {
        runOnUiThread(() -> webView.loadDataWithBaseURL(
                null,
                "<html><body style='margin:0;font-family:sans-serif;background:#f8fbff;color:#0f172a;display:flex;align-items:center;justify-content:center;height:100vh;'>" +
                "<div style='text-align:center;padding:24px'>" +
                "<h2>Muavin Asistanı açılıyor...</h2>" +
                "<p>Flask sunucusu başlatılıyor. Lütfen bekle.</p>" +
                "</div></body></html>",
                "text/html",
                "UTF-8",
                null
        ));
    }

    private void showError(String message) {
        String err = message
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;");

        runOnUiThread(() -> webView.loadDataWithBaseURL(
                null,
                "<html><body style='font-family:sans-serif;padding:22px;background:#f8fbff;color:#0f172a;'>" +
                "<h2>Muavin Asistanı başlatılamadı</h2>" +
                "<p>APK içindeki Flask sunucusu açılırken sorun oluştu.</p>" +
                "<pre style='white-space:pre-wrap;background:#111827;color:#fff;padding:14px;border-radius:12px;font-size:13px;'>" + err + "</pre>" +
                "</body></html>",
                "text/html",
                "UTF-8",
                null
        ));
    }

    private void requestBasicPermissions() {
        if (android.os.Build.VERSION.SDK_INT >= 23) {
            requestPermissions(new String[]{
                    Manifest.permission.ACCESS_FINE_LOCATION,
                    Manifest.permission.ACCESS_COARSE_LOCATION,
                    Manifest.permission.CAMERA,
                    Manifest.permission.RECORD_AUDIO
            }, 100);
        }
    }


    @Override
    protected void onDestroy() {
        try {
            if (tts != null) {
                tts.stop();
                tts.shutdown();
            }
        } catch (Exception ignored) {}

        super.onDestroy();
    }

    @Override
    public void onBackPressed() {
        if (webView != null && webView.canGoBack()) {
            webView.goBack();
        } else {
            super.onBackPressed();
        }
    }
}
