package guru.springframework.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import guru.springframework.services.ProductService;

@Controller
public class IndexController {
	
	ProductService productService;

	@RequestMapping("/")
	public String getIndex(Model model){
		model.addAttribute("products", productService.listProducts());
		return "index";
	}

	public ProductService getProductService() {
		return productService;
	}

	@Autowired
	public void setProductService(ProductService productService) {
		this.productService = productService;
	}
	
	
}
