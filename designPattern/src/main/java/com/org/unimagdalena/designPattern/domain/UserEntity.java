package com.org.unimagdalena.designPattern.domain;

import jakarta.persistence.*;
import lombok.Data;

import java.time.LocalDateTime;

@Data
@Entity
@Table(name = "user_user")
public class UserEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "password")
    private String password;

    @Column(name = "last_login")
    private LocalDateTime lastLogin;

    @Column(name = "created_at")
    private LocalDateTime createdAt;

    @Column(name = "updated_at")
    private LocalDateTime updatedAt;

    @Column(name = "deleted_at")
    private LocalDateTime deletedAt;

    @Column(name = "is_active")
    private Boolean isActive;

    @Column(name = "email")
    private String email;

    @Column(name = "first_name")
    private String firstName;

    @Column(name = "last_name")
    private String lastName;

    @Column(name = "document")
    private String document;

    @Column(name = "code_phone")
    private String codePhone;

    @Column(name = "phone_number")
    private String phoneNumber;

    @Column(name = "is_admin")
    private Boolean isAdmin;

    @Column(name = "is_superuser")
    private Boolean isSuperUser;

    @Column(name = "profile_image")
    private String profileImage;

    @Column(name = "city")
    private String city;

}
