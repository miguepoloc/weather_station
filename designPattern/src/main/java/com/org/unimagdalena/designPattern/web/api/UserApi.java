package com.org.unimagdalena.designPattern.web.api;

import com.org.unimagdalena.designPattern.web.api.model.UserResponse;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

public interface UserApi {

    @GetMapping(value = "api/unimagdalena/user",
            produces = { "application/json" })
    default ResponseEntity<List<UserResponse>> getAllUser() {
        return new ResponseEntity<List<UserResponse>>(HttpStatus.OK);
    }

}