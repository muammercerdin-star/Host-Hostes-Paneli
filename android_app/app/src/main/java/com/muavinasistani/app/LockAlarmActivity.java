package com.muavinasistani.app;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.Typeface;
import android.os.Build;
import android.os.Bundle;
import android.view.Gravity;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.util.Locale;

public class LockAlarmActivity extends Activity {
    private static final String PREF = "muavin_lock_alarm_v85";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        try {
            getWindow().addFlags(
                    WindowManager.LayoutParams.FLAG_SHOW_WHEN_LOCKED
                            | WindowManager.LayoutParams.FLAG_TURN_SCREEN_ON
                            | WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON
            );

            if (Build.VERSION.SDK_INT >= 27) {
                setShowWhenLocked(true);
                setTurnScreenOn(true);
            }
        } catch (Exception ignored) {}

        buildUi();
    }

    private String clean(String v) {
        return v == null ? "" : v.trim();
    }

    private void buildUi() {
        SharedPreferences prefs = getSharedPreferences(PREF, MODE_PRIVATE);

        String stopName = clean(prefs.getString("stop_name", "Canlı durak"));
        String km = clean(prefs.getString("display_km", ""));
        if (km.length() == 0) km = "2 km";

        int offload = 0;
        int bag = 0;

        try {
            offload = Integer.parseInt(prefs.getString("offload_count", "0"));
        } catch (Exception ignored) {}

        try {
            bag = Integer.parseInt(prefs.getString("bag_count", "0"));
        } catch (Exception ignored) {}

        String yolcu = offload > 0 ? offload + " yolcu inecek" : "İnecek yolcu yok";
        String bagaj = bag > 0 ? bag + " bagaj var" : "0 bagaj";

        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        root.setGravity(Gravity.CENTER);
        root.setPadding(42, 42, 42, 42);
        root.setBackgroundColor(Color.rgb(10, 12, 20));

        TextView badge = new TextView(this);
        badge.setText("CANLI DURAK ALARMI");
        badge.setTextColor(Color.rgb(255, 45, 96));
        badge.setTextSize(18);
        badge.setTypeface(Typeface.DEFAULT_BOLD);
        badge.setLetterSpacing(0.14f);
        badge.setGravity(Gravity.CENTER);
        root.addView(badge, new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
        ));

        TextView stop = new TextView(this);
        stop.setText(stopName.toLocaleUpperCase(new Locale("tr", "TR")));
        stop.setTextColor(Color.WHITE);
        stop.setTextSize(48);
        stop.setTypeface(Typeface.DEFAULT_BOLD);
        stop.setGravity(Gravity.CENTER);
        stop.setPadding(0, 28, 0, 8);
        root.addView(stop, new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
        ));

        TextView dist = new TextView(this);
        dist.setText("Kalan mesafe: " + km);
        dist.setTextColor(Color.rgb(230, 230, 235));
        dist.setTextSize(24);
        dist.setTypeface(Typeface.DEFAULT_BOLD);
        dist.setGravity(Gravity.CENTER);
        dist.setPadding(0, 4, 0, 22);
        root.addView(dist, new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
        ));

        TextView info = new TextView(this);
        info.setText(yolcu + "  •  " + bagaj);
        info.setTextColor(Color.rgb(220, 220, 225));
        info.setTextSize(22);
        info.setGravity(Gravity.CENTER);
        info.setPadding(0, 0, 0, 38);
        root.addView(info, new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
        ));

        Button stopBtn = new Button(this);
        stopBtn.setText("ALARMı DURDUR");
        stopBtn.setTextSize(20);
        stopBtn.setTypeface(Typeface.DEFAULT_BOLD);
        stopBtn.setTextColor(Color.WHITE);
        stopBtn.setBackgroundColor(Color.rgb(255, 45, 96));
        stopBtn.setAllCaps(false);
        stopBtn.setOnClickListener(v -> {
            try {
                Intent i = new Intent(this, LiveStopAlertService.class);
                i.setAction(LiveStopAlertService.ACTION_STOP_ALARM);
                startService(i);
            } catch (Exception ignored) {}
            finish();
        });

        LinearLayout.LayoutParams stopLp = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                120
        );
        stopLp.setMargins(0, 0, 0, 22);
        root.addView(stopBtn, stopLp);

        Button openBtn = new Button(this);
        openBtn.setText("Uygulamayı aç");
        openBtn.setTextSize(18);
        openBtn.setAllCaps(false);
        openBtn.setOnClickListener(v -> {
            try {
                Intent i = new Intent(this, MainActivity.class);
                i.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
                startActivity(i);
            } catch (Exception ignored) {}
            finish();
        });

        LinearLayout.LayoutParams openLp = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                105
        );
        root.addView(openBtn, openLp);

        setContentView(root);
    }
}
