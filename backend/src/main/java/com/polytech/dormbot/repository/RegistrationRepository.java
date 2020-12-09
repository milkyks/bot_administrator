package com.polytech.dormbot.repository;

import com.polytech.dormbot.entity.Registration;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface RegistrationRepository extends JpaRepository<Registration, Long> {

    List<Registration> findAllByUser_Id(Long id);
}
