package com.polytech.dormbot.api.v1.dto;

import lombok.Data;

import java.util.Date;

@Data
public class DutyData {
    private Long id;
    private Integer roomNumber;
    private Date date;
}
