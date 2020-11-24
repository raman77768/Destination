package com.example.may_app_1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

public class OrderActivity extends AppCompatActivity {

    private TextView mname,mprofile,mstipend,mlink;
    private ImageView mImageView;
    private Button button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_order);
        mname = findViewById(R.id.nameText);
        mprofile = findViewById(R.id.profileText);
        mstipend = findViewById(R.id.descText);
        mImageView=findViewById(R.id.display_image);
        button = findViewById(R.id.button);

        Intent intent = getIntent();
        String companyname = intent.getStringExtra("name");
        String profile = intent.getStringExtra("profile");
        String stipend = intent.getStringExtra("desc");
        final String link = intent.getStringExtra("link");
        String thumb = intent.getStringExtra("thumb");

        mname.setText(companyname);
        mprofile.setText(profile);
        mstipend.setText(stipend);


        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Uri uri = Uri.parse(link);
                startActivity(new Intent(Intent.ACTION_VIEW,uri));
            }
        });

    }
}
