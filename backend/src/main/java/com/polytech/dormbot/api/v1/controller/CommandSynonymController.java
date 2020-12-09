package com.polytech.dormbot.api.v1.controller;

import com.polytech.dormbot.api.v1.dto.CommandSynonymData;
import com.polytech.dormbot.api.v1.dto.Mapper;
import com.polytech.dormbot.entity.CommandSynonym;
import com.polytech.dormbot.service.CommandSynonymService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.stream.Collectors;

@RestController
@CrossOrigin()
@RequestMapping("/api/v1/command_synonyms")
public class CommandSynonymController {
    private final CommandSynonymService commandSynonymService;
    private final Mapper mapper;

    @Autowired
    public CommandSynonymController(CommandSynonymService commandSynonymService, Mapper mapper) {
        this.commandSynonymService = commandSynonymService;
        this.mapper = mapper;
    }

    @GetMapping
    public List<CommandSynonymData> getCommandSynonymsByCommandId(@RequestParam Long commandId){
        return commandSynonymService.getCommandSynonymsByCommandId(commandId)
                .stream()
                .map(mapper::convertToData)
                .collect(Collectors.toList());
    }

    @GetMapping(value = "/{id}")
    public CommandSynonymData getSynonym(@PathVariable Long id) {
        return mapper.convertToData(commandSynonymService.getCommandSynonym(id));
    }

    @PostMapping
    public CommandSynonymData addCommandSynonym(@RequestBody CommandSynonymData commandSynonymData){
        CommandSynonym commandSynonym = mapper.convertToEntity(commandSynonymData);

        return mapper.convertToData(commandSynonymService.addCommandSynonym(commandSynonym));
    }

    @DeleteMapping(value = "/{id}")
    public void deleteCommandSynonym(@PathVariable Long id) {
        commandSynonymService.deleteCommandSynonym(id);
    }
}
