package com.org.unimagdalena.designPattern.service.impl;

import com.org.unimagdalena.designPattern.mapper.UserMapper;
import com.org.unimagdalena.designPattern.repository.UserRepository;
import com.org.unimagdalena.designPattern.service.interfaz.UserService;
import com.org.unimagdalena.designPattern.web.api.model.UserResponse;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
@AllArgsConstructor
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;

    @Override
    public List<UserResponse> getAllUser() {
        return userRepository.findAll()
                .stream()
                .map(UserMapper.MAPPER::toUserResponse)
                .toList();
    }
}
