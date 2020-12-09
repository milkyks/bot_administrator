package com.polytech.dormbot.api.v1.dto;

import lombok.Data;

import java.util.Set;

@Data
public class CommandData {
    private Long id;
    private String name;
    private Boolean isActive;
    private Set<CommandStatisticData> commandStatistics;
    private Set<CommandSynonymData> commandSynonyms;
}
