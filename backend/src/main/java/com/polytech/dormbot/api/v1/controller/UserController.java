package com.polytech.dormbot.api.v1.controller;

import com.polytech.dormbot.api.v1.dto.Mapper;
import com.polytech.dormbot.api.v1.dto.UserData;
import com.polytech.dormbot.entity.User;
import com.polytech.dormbot.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@CrossOrigin()
@RequestMapping("/api/v1/users")
public class UserController {
    private final UserService userService;
    private final Mapper mapper;

    @Autowired
    public UserController(UserService userService, Mapper mapper) {
        this.userService = userService;
        this.mapper = mapper;
    }

    @GetMapping(value = "/{id}")
    public UserData getUser(@PathVariable Long id) {
        return mapper.convertToData(userService.getUser(id));
    }

    @PostMapping
    public UserData addUser(@RequestBody UserData userData){
        User user = mapper.convertToEntity(userData);
        return mapper.convertToData(userService.addUser(user));
    }

    @DeleteMapping(value = "/{id}")
    public void deleteDuty(@PathVariable Long id) {
        userService.deleteUser(id);
    }
}
