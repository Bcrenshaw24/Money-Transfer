package com.bank.eventservice.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.bank.eventservice.model.Transaction;

public interface TransactionRepository extends JpaRepository<Transaction, Long> {
}
