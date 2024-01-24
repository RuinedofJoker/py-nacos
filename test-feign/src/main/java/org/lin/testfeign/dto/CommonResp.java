package org.lin.testfeign.dto;

import lombok.Data;
import lombok.experimental.Accessors;

@Data
@Accessors(chain = true)
public class CommonResp<D> {
    private Integer code;
    private String msg;
    private D data;
}
