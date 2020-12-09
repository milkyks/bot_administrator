package com.polytech.dormbot.api.v1.dto;

import lombok.Data;

import java.util.Date;

@Data
public class CommandStatisticData {
    private Long id;
    private Long vkId;
    private Date date;
    private Long commandId;
}
