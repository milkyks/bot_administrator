package com.polytech.dormbot.api.v1.exception;

import com.polytech.dormbot.exception.NoSuchCommandException;
import com.polytech.dormbot.exception.NoSuchDutyException;
import com.polytech.dormbot.exception.NoSuchRegistrationException;
import com.polytech.dormbot.exception.NoSuchUserException;
import lombok.AllArgsConstructor;
import lombok.Data;
import org.springframework.core.Ordered;
import org.springframework.core.annotation.Order;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

@Order(Ordered.HIGHEST_PRECEDENCE)
@ControllerAdvice
public class CustomExceptionHandler extends ResponseEntityExceptionHandler {

    @ExceptionHandler(NoSuchCommandException.class)
    protected ResponseEntity<Exception> handleNoSuchNotebookException() {
        return new ResponseEntity<>(new Exception(400, "No such command"), HttpStatus.BAD_REQUEST);
    }

    @ExceptionHandler(NoSuchUserException.class)
    protected ResponseEntity<Exception> handleNoSuchUserException() {
        return new ResponseEntity<>(new Exception(400, "No such user"), HttpStatus.BAD_REQUEST);
    }

    @ExceptionHandler(NoSuchDutyException.class)
    protected ResponseEntity<Exception> handleNoSuchDutyException() {
        return new ResponseEntity<>(new Exception(400, "No such duty"), HttpStatus.BAD_REQUEST);
    }

    @ExceptionHandler(NoSuchRegistrationException.class)
    protected ResponseEntity<Exception> handleNoSuchRegistrationException() {
        return new ResponseEntity<>(new Exception(400, "No such registration"), HttpStatus.BAD_REQUEST);
    }


    @Data
    @AllArgsConstructor
    private static class Exception{
        private int code;
        private String message;
    }
}
