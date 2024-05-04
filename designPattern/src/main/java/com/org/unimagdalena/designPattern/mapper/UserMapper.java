package com.org.unimagdalena.designPattern.mapper;

import com.org.unimagdalena.designPattern.domain.UserEntity;
import com.org.unimagdalena.designPattern.web.api.model.UserResponse;
import org.mapstruct.Mapper;
import org.mapstruct.factory.Mappers;

@Mapper
public interface UserMapper {

    UserMapper MAPPER = Mappers.getMapper(UserMapper.class);

    UserResponse toUserResponse(UserEntity userEntity);
}
