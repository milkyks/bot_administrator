package com.polytech.dormbot.api.v1.controller;

import com.polytech.dormbot.api.v1.dto.Mapper;
import com.polytech.dormbot.api.v1.dto.RegistrationData;
import com.polytech.dormbot.entity.Registration;
import com.polytech.dormbot.service.RegistrationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.stream.Collectors;

@RestController
@CrossOrigin()
@RequestMapping("/api/v1/registration")
public class RegistrationController {
    private final RegistrationService registrationService;
    private final Mapper mapper;

    @Autowired
    public RegistrationController(RegistrationService registrationService, Mapper mapper) {
        this.registrationService = registrationService;
        this.mapper = mapper;
    }

    @GetMapping(value = "/{id}")
    public RegistrationData getRegistration(@PathVariable Long id) {
        return mapper.convertToData(registrationService.getRegistration(id));
    }

    @GetMapping
    public List<RegistrationData> getRegistrationsByUserId(@RequestParam Long userId) {
        return registrationService.getRegistrationsByUserId(userId)
                .stream()
                .map(mapper::convertToData)
                .collect(Collectors.toList());
    }

    @PostMapping
    public RegistrationData addRegistration(@RequestBody RegistrationData registrationData){
        Registration registration = mapper.convertToEntity(registrationData);

        return mapper.convertToData(registrationService.addRegistration(registration));
    }

    @DeleteMapping(value = "/{id}")
    public void deleteRegistration(@PathVariable Long id) {
        registrationService.deleteRegistration(id);
    }
}
