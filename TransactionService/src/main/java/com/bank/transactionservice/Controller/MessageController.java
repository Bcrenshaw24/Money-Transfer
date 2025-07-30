package com.bank.transactionservice.Controller;

import com.bank.transactionservice.Request.Request;
import com.bank.transactionservice.config.RabbitMQConfig;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.stereotype.Service;

@Service
public class MessageController {
    private final RabbitTemplate rabbitTemplate;

    public MessageController(RabbitTemplate rabbitTemplate) {
        this.rabbitTemplate = rabbitTemplate;
    }

    public void send(Request message) {
        rabbitTemplate.convertAndSend(
                RabbitMQConfig.EXCHANGE,       // use exchange from your config class
                RabbitMQConfig.ROUTING_KEY,    // use routing key from your config class
                message                        // the actual message
        );
    }
}
