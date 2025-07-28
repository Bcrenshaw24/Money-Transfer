package com.bank.transactionservice.service;

import com.bank.transactionservice.model.Transaction;
import org.springframework.stereotype.Service;

@Service
public class TransactionService {

    public boolean isValid(Transaction account) {
        return !(account.getAmount() <= 0);
    }

    public void processTransaction (Transaction account) {
        if (!isValid(account)) {
            throw new IllegalArgumentException("Invalid Transaction!");
        }

    }


}
