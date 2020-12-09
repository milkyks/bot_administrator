package com.polytech.dormbot.entity;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import javax.persistence.*;
import java.util.Set;

@Entity
@Getter
@Setter
@ToString
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy=GenerationType.IDENTITY)
    @Column(name = "id", nullable = false, unique = true)
    private Long id;

    @Column(name = "full_name", nullable = false)
    private String fullName;

    @Column(name = "vk_id", nullable = false)
    private Long vkId;

    @Column(name = "room_number", nullable = false)
    private Integer roomNumber;

    @Column(name = "phone_number", nullable = false)
    private String phoneNumber;

    @OneToMany(mappedBy = "user", cascade = CascadeType.REMOVE)
    private Set<Registration> registrations;
}
