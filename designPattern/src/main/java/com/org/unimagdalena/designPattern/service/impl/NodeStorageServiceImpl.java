package com.org.unimagdalena.designPattern.service.impl;

import com.org.unimagdalena.designPattern.mapper.NodeStorageMapper;
import com.org.unimagdalena.designPattern.mapper.UserMapper;
import com.org.unimagdalena.designPattern.repository.NodeStorageRepository;
import com.org.unimagdalena.designPattern.repository.UserRepository;
import com.org.unimagdalena.designPattern.service.interfaz.AlertHandler;
import com.org.unimagdalena.designPattern.service.interfaz.NodeStorageService;
import com.org.unimagdalena.designPattern.service.interfaz.UserService;
import com.org.unimagdalena.designPattern.web.api.model.NodeStorageResponse;
import com.org.unimagdalena.designPattern.web.api.model.UserResponse;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@AllArgsConstructor
public class NodeStorageServiceImpl implements NodeStorageService {

    private final NodeStorageRepository nodeStorageRepository;
    private final AlertHandler temperatureHandler;


    @Override
    public List<NodeStorageResponse> getAllNodeStorage() {
        return nodeStorageRepository.findAll()
                .stream()
                .map(NodeStorageMapper.MAPPER::toNodeStorageResponse)
                .toList();
    }

    @Override
    public String getStatusMeteorologyCenter() {
        NodeStorageResponse nodeStorageResponse = nodeStorageRepository.findAll()
                .stream()
                .map(NodeStorageMapper.MAPPER::toNodeStorageResponse)
                .findFirst()
                .orElse(null);

        return temperatureHandler.handleRequest(nodeStorageResponse);
    }
}
