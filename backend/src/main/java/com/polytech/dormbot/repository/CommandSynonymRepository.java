package com.polytech.dormbot.repository;

import com.polytech.dormbot.entity.CommandSynonym;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CommandSynonymRepository extends JpaRepository<CommandSynonym, Long> {
    List<CommandSynonym> findAllByCommand_Id(Long id);
}
