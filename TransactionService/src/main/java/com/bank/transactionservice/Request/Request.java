package com.bank.transactionservice.Request;
import lombok.Getter;

import java.util.Map;

public class Request {
    @Getter
    private final String action;
    @Getter
    private final String userId;
    @Getter
    private final Map<String, Object> payload;
    public Request(String action, String userId, Map<String, Object> payload) {
        this.action = action;
        this.userId = userId;
        this.payload = payload;
    }

}
