package com.polytech.dormbot.service;

import com.polytech.dormbot.entity.Command;
import com.polytech.dormbot.exception.NoSuchCommandException;
import com.polytech.dormbot.repository.CommandRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CommandService {
    private final CommandRepository commandRepository;

    @Autowired
    public CommandService(CommandRepository commandRepository) {
        this.commandRepository = commandRepository;
    }

    public List<Command> getAll() {
        return commandRepository.findAll();
    }

    public Command getCommand(Long id) {
        return commandRepository.findById(id).orElseThrow(NoSuchCommandException::new);
    }

    public Command addCommand(Command command) {
        return commandRepository.save(command);
    }

    public void deleteCommand(Long id) {
        commandRepository.deleteById(id);
    }

}
