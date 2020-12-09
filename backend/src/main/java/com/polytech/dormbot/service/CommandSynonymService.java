package com.polytech.dormbot.service;

import com.polytech.dormbot.entity.Command;
import com.polytech.dormbot.entity.CommandSynonym;
import com.polytech.dormbot.exception.NoSuchCommandException;
import com.polytech.dormbot.exception.NoSuchCommandSynonymException;
import com.polytech.dormbot.repository.CommandSynonymRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CommandSynonymService {
    private final CommandSynonymRepository commandSynonymRepository;

    @Autowired
    public CommandSynonymService(CommandSynonymRepository commandSynonymRepository) {
        this.commandSynonymRepository = commandSynonymRepository;
    }

    public CommandSynonym getCommandSynonym(Long id) {
        return commandSynonymRepository.findById(id).orElseThrow(NoSuchCommandSynonymException::new);
    }

    public List<CommandSynonym> getCommandSynonymsByCommandId(Long commandId) {
        return commandSynonymRepository.findAllByCommand_Id(commandId);
    }

    public CommandSynonym addCommandSynonym(CommandSynonym commandSynonym) {
        return commandSynonymRepository.save(commandSynonym);
    }

    public void deleteCommandSynonym(Long id) {
        commandSynonymRepository.deleteById(id);
    }
}
