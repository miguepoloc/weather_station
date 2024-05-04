package com.org.unimagdalena.designPattern.mapper;

import com.org.unimagdalena.designPattern.domain.NodeStorageEntity;
import com.org.unimagdalena.designPattern.web.api.model.NodeStorageResponse;
import org.mapstruct.Mapper;
import org.mapstruct.factory.Mappers;

@Mapper
public interface NodeStorageMapper {

    NodeStorageMapper MAPPER = Mappers.getMapper(NodeStorageMapper.class);

    NodeStorageResponse toNodeStorageResponse(NodeStorageEntity nodeStorageEntity);
}
