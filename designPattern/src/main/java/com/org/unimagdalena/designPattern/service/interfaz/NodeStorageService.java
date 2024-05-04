package com.org.unimagdalena.designPattern.service.interfaz;

import com.org.unimagdalena.designPattern.web.api.model.NodeStorageResponse;
import com.org.unimagdalena.designPattern.web.api.model.UserResponse;

import java.util.List;

public interface NodeStorageService {
    public List<NodeStorageResponse> getAllNodeStorage();

    public String getStatusMeteorologyCenter();
}
