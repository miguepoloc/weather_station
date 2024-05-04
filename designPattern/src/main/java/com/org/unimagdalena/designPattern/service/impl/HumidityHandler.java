package com.org.unimagdalena.designPattern.service.impl;

import com.org.unimagdalena.designPattern.web.api.model.NodeStorageResponse;
import org.springframework.stereotype.Component;

@Component
public class HumidityHandler extends BaseAlertHandlerImpl{

    @Override
    public String handleRequest(NodeStorageResponse nodeStorageResponse) {
        if (nodeStorageResponse.getHumidity().intValue() > 40) {
            return String.valueOf("Precaucion: Nivel de humedad alta. Humedad: " + nodeStorageResponse.getHumidity().intValue() + "%" );
        } else {
            if (nextHandler != null) {
                return nextHandler.handleRequest(nodeStorageResponse);
            }
        }
        return null;
    }
}
