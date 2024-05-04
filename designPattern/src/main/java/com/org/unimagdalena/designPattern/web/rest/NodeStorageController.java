package com.org.unimagdalena.designPattern.web.rest;

import com.org.unimagdalena.designPattern.service.interfaz.NodeStorageService;
import com.org.unimagdalena.designPattern.service.interfaz.UserService;
import com.org.unimagdalena.designPattern.web.api.NodeStorageApi;
import com.org.unimagdalena.designPattern.web.api.UserApi;
import com.org.unimagdalena.designPattern.web.api.model.NodeStorageResponse;
import com.org.unimagdalena.designPattern.web.api.model.UserResponse;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@Slf4j
@RestController
public class NodeStorageController implements NodeStorageApi {

    private final NodeStorageService nodeStorageService;

    public NodeStorageController(NodeStorageService nodeStorageService) {
        this.nodeStorageService = nodeStorageService;
    }

    @Override
    public ResponseEntity<List<NodeStorageResponse>> getAllNodeStorage() {
        return ResponseEntity.ok(nodeStorageService.getAllNodeStorage());
    }

    @Override
    public ResponseEntity<String> getStatusMeteorologyCenter() {
        return ResponseEntity.ok(nodeStorageService.getStatusMeteorologyCenter());
    }
}
