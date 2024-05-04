package com.org.unimagdalena.designPattern.web.api.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;

import java.time.LocalDateTime;

@Data
@AllArgsConstructor
@Builder
public class UserResponse {

    private Long id;
    private String password;
    private LocalDateTime lastLogin;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
    private LocalDateTime deletedAt;
    private Boolean isActive;
    private String email;
    private String firstName;
    private String lastName;
    private String document;
    private String codePhone;
    private String phoneNumber;
    private Boolean isAdmin;
    private Boolean isSuperUser;
    private String profileImage;
    private String city;

}