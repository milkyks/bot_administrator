package com.polytech.dormbot.service;

import com.polytech.dormbot.entity.Registration;
import com.polytech.dormbot.exception.NoSuchRegistrationException;
import com.polytech.dormbot.repository.RegistrationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class RegistrationService {
    private final RegistrationRepository registrationRepository;

    @Autowired
    public RegistrationService(RegistrationRepository registrationRepository) {
        this.registrationRepository = registrationRepository;
    }

    public Registration getRegistration(Long id) {
        return registrationRepository.findById(id).orElseThrow(NoSuchRegistrationException::new);
    }

    public List<Registration> getRegistrationsByUserId(Long userId) {
        return registrationRepository.findAllByUser_Id(userId);
    }

    public Registration addRegistration(Registration registration) {
        return registrationRepository.save(registration);
    }

    public void deleteRegistration(Long id) {
        registrationRepository.deleteById(id);
    }
}
