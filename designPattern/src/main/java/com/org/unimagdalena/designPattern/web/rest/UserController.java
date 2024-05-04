package com.org.unimagdalena.designPattern.web.rest;

import com.org.unimagdalena.designPattern.service.interfaz.UserService;
import com.org.unimagdalena.designPattern.web.api.UserApi;
import com.org.unimagdalena.designPattern.web.api.model.UserResponse;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@Slf4j
@RestController
public class UserController implements UserApi {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @Override
    public ResponseEntity<List<UserResponse>> getAllUser() {
        return ResponseEntity.ok(userService.getAllUser());
    }
}
