package com.bank.transactionservice.Controller;

import com.bank.transactionservice.Request.Request;
import com.bank.transactionservice.Validation.Validation;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/transaction")
public class TransactionController {
    private Validation validator;
    private final MessageController messenger;

    public TransactionController(MessageController messenger) {
        this.messenger = messenger;
    }

    public ResponseEntity<String> verifyUser(Request user) {
        Object balanceObj = user.getPayload().get("balance");
        if (balanceObj != null) {
            double balance = Double.parseDouble(balanceObj.toString());
            if (!validator.isValid(balance)) {
                return ResponseEntity.badRequest().body("Insufficient balance");
            }
            try {
                messenger.send(user);
                return ResponseEntity.ok("Transaction initiated");
            }
            catch (Exception e) {
                return ResponseEntity.badRequest().body("Transaction Failed");
            }
        }
        else {
            return ResponseEntity.badRequest().body("Balance not found");
        }
    }
}


