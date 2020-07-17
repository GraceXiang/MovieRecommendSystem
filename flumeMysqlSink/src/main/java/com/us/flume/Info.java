package com.us.flume;

/**
 * Created by xianglingrui on 20/7/16.
 */
public class Info {
    private String time;
    private String message;

    public String getContent() {
        return time;
    }

    public void setContent(String time) {
        this.time = time;
    }

    public String getCreateBy() {
        return message;
    }

    public void setCreateBy(String message) {
        this.message = message;
    }
}
