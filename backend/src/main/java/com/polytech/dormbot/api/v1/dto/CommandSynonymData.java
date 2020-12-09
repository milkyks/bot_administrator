package com.polytech.dormbot.api.v1.dto;

import lombok.Data;

@Data
public class CommandSynonymData {
    private Long id;
    private String synonym;
    private Long commandId;
}
