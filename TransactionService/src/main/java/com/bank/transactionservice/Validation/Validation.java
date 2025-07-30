package com.bank.transactionservice.Validation;

public class Validation {

    public boolean isValid(double balance) {
        return !(balance < 0);
    }
}
