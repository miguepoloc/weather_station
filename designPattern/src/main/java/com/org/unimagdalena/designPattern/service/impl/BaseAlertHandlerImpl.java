package com.org.unimagdalena.designPattern.service.impl;

import com.org.unimagdalena.designPattern.service.interfaz.AlertHandler;
import com.org.unimagdalena.designPattern.web.api.model.NodeStorageResponse;
import lombok.Data;

@Data
public abstract class BaseAlertHandlerImpl implements AlertHandler {

    protected AlertHandler nextHandler;

    public void setNextHandler(AlertHandler nextHandler) {
        this.nextHandler = nextHandler;
    }

    public abstract String handleRequest(NodeStorageResponse nodeStorageResponse);

}
