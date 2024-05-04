package com.org.unimagdalena.designPattern.service.interfaz;

import com.org.unimagdalena.designPattern.web.api.model.UserResponse;

import java.util.List;

public interface UserService {
    public List<UserResponse> getAllUser();
}
