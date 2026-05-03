package com.muavinasistani.app;

import android.Manifest;
import android.app.Activity;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.webkit.WebResourceError;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class MainActivity extends Activity {
    private WebView webView;
    private boolean pageLoaded = false;

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

        webView.setWebViewClient(new WebViewClient() {
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
                py.getModule("android_server").callAttr("start_in_background");

                runOnUiThread(() -> {
                    webView.loadUrl("http://127.0.0.1:5000/");
                });

            } catch (Exception e) {
                showError("Flask sunucusu başlatılamadı:\n" + e.toString());
            }
        }).start();

        new Handler(Looper.getMainLooper()).postDelayed(() -> {
            if (!pageLoaded) {
                showError(
                    "Uygulama zamanında açılmadı.\n\n" +
                    "Flask sunucusu APK içinde başlamamış olabilir.\n" +
                    "Bir sonraki adımda Python hata çıktısını ayrıca loglayacağız."
                );
            }
        }, 35000);
    }

    private void showLoading() {
        runOnUiThread(() -> {
            webView.loadDataWithBaseURL(
                null,
                "<html><body style='margin:0;font-family:sans-serif;background:#f8fbff;color:#0f172a;display:flex;align-items:center;justify-content:center;height:100vh;'>" +
                "<div style='text-align:center;padding:24px'>" +
                "<h2>Muavin Asistanı açılıyor...</h2>" +
                "<p>Flask sunucusu başlatılıyor. Lütfen bekle.</p>" +
                "</div>" +
                "</body></html>",
                "text/html",
                "UTF-8",
                null
            );
        });
    }

    private void showError(String message) {
        String err = message
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;");

        runOnUiThread(() -> {
            webView.loadDataWithBaseURL(
                null,
                "<html><body style='font-family:sans-serif;padding:22px;background:#f8fbff;color:#0f172a;'>" +
                "<h2>Muavin Asistanı başlatılamadı</h2>" +
                "<p>APK içindeki Flask sunucusu açılırken sorun oluştu.</p>" +
                "<pre style='white-space:pre-wrap;background:#111827;color:#fff;padding:14px;border-radius:12px;font-size:13px;'>" + err + "</pre>" +
                "</body></html>",
                "text/html",
                "UTF-8",
                null
            );
        });
    }

    private void requestBasicPermissions() {
        if (android.os.Build.VERSION.SDK_INT >= 23) {
            requestPermissions(new String[]{
                Manifest.permission.ACCESS_FINE_LOCATION,
                Manifest.permission.ACCESS_COARSE_LOCATION,
                Manifest.permission.CAMERA
            }, 100);
        }
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
