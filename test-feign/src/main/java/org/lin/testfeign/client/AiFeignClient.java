package org.lin.testfeign.client;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;

@FeignClient(value = "tendering-ai", contextId = "aiFeignClient", path = "/ai")
public interface AiFeignClient {

    @GetMapping("/test")
    public String testAi();
}
