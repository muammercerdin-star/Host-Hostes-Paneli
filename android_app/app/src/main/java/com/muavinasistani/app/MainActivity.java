package com.muavinasistani.app;

import android.Manifest;
import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class MainActivity extends Activity {
    private WebView webView;

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

        webView.setWebViewClient(new WebViewClient());

        if (!Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }

        new Thread(() -> {
            try {
                Python py = Python.getInstance();
                py.getModule("android_server").callAttr("start_in_background");

                runOnUiThread(() -> {
                    webView.loadUrl("http://127.0.0.1:5000/");
                });

            } catch (Exception e) {
                String err = e.toString()
                    .replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;");

                runOnUiThread(() -> {
                    webView.loadData(
                        "<html><body style='font-family:sans-serif;padding:24px;background:#f8fbff;color:#0f172a;'>" +
                        "<h2>Muavin Asistanı başlatılamadı</h2>" +
                        "<p>Flask sunucusu APK içinde açılırken hata verdi.</p>" +
                        "<pre style='white-space:pre-wrap;background:#111827;color:#fff;padding:14px;border-radius:12px;'>" + err + "</pre>" +
                        "</body></html>",
                        "text/html",
                        "UTF-8"
                    );
                });
            }
        }).start();
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
