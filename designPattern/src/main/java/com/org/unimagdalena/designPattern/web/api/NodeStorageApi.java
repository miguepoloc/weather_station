package com.org.unimagdalena.designPattern.web.api;

import com.org.unimagdalena.designPattern.web.api.model.NodeStorageResponse;
import com.org.unimagdalena.designPattern.web.api.model.UserResponse;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

public interface NodeStorageApi {

    @GetMapping(value = "api/unimagdalena/nodeStorage",
            produces = { "application/json" })
    default ResponseEntity<List<NodeStorageResponse>> getAllNodeStorage() {
        return new ResponseEntity<List<NodeStorageResponse>>(HttpStatus.OK);
    }

    @GetMapping(value = "api/unimagdalena/statusMeteorologyCenter",
            produces = { "application/json" })
    default ResponseEntity<String> getStatusMeteorologyCenter() {
        return new ResponseEntity<String>(HttpStatus.OK);
    }
}
