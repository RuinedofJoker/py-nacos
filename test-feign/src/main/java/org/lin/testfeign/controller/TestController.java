package org.lin.testfeign.controller;

import org.lin.testfeign.client.AiFeignClient;
import org.lin.testfeign.client.RandomInfoFeignClient;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.openfeign.FeignClientsConfiguration;
import org.springframework.context.annotation.Import;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@Import(FeignClientsConfiguration.class)
@RestController
public class TestController {

    @Autowired
    private RandomInfoFeignClient randomInfoFeignClient;

    @Autowired
    private AiFeignClient aiFeignClient;


    @GetMapping("/test")
    public String test() {
        //return JSON.toJSONString(randomInfoFeignClient.randomIdCard(null, null, "2020-01-01", null));
        return aiFeignClient.testAi();
    }
}
