package com.polytech.dormbot.entity;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import javax.persistence.*;
import java.util.Set;

@Getter
@Setter
@ToString
@Entity
@Table(name = "commands")
public class Command {
    @Id
    @GeneratedValue(strategy=GenerationType.IDENTITY)
    @Column(name = "id", nullable = false, unique = true)
    private Long id;

    @Column(name = "name")
    private String name;

    @Column(name = "is_active")
    private Boolean isActive;

    @OneToMany(mappedBy = "command", cascade = CascadeType.REMOVE)
    private Set<CommandStatistic> commandStatistics;

    @OneToMany(mappedBy = "command", cascade = CascadeType.REMOVE)
    private Set<CommandSynonym> commandSynonyms;
}
