package com.example.may_app_1;

import androidx.lifecycle.ViewModel;

public class MainViewModel extends ViewModel {
    public String name,link,desc,profile,thumb;

    public MainViewModel(String name, String link, String desc, String profile,String thumb) {
        this.name = name;
        this.link = link;
        this.desc = desc;
        this.profile = profile;
        this.thumb=thumb;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }

    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }

    public String getProfile() {
        return profile;
    }


}
