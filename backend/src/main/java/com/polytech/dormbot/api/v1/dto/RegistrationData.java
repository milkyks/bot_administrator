package com.polytech.dormbot.api.v1.dto;

import lombok.Data;

import java.util.Date;

@Data
public class RegistrationData {
    private Long id;
    private String roomType;
    private Date date;
    private Long userId;
}
