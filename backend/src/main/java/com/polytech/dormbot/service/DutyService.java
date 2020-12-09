package com.polytech.dormbot.service;

import com.polytech.dormbot.entity.Duty;
import com.polytech.dormbot.exception.NoSuchDutyException;
import com.polytech.dormbot.repository.DutyRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class DutyService {
    private final DutyRepository dutyRepository;

    @Autowired
    public DutyService(DutyRepository dutyRepository) {
        this.dutyRepository = dutyRepository;
    }

    public List<Duty> getAll() {
        return dutyRepository.findAll();
    }

    public Duty getDuty(Long id) {
        return dutyRepository.findById(id).orElseThrow(NoSuchDutyException::new);
    }

    public Duty addDuty(Duty duty) {
        return dutyRepository.save(duty);
    }

    public void deleteDuty(Long id) {
        dutyRepository.deleteById(id);
    }
}
