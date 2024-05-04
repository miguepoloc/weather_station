package com.org.unimagdalena.designPattern.service.interfaz;

import com.org.unimagdalena.designPattern.web.api.model.NodeStorageResponse;

public interface AlertHandler {
    String handleRequest(NodeStorageResponse nodeStorageResponse);
}
