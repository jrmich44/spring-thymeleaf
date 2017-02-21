package guru.springframework.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import guru.springframework.services.ProductService;

/**
 * Created by jt on 1/20/16.
 */
@Controller
public class ProductController {
	
	private ProductService productService;

    @RequestMapping("/product")
    public String getProduct(){
        return "redirect:/";
    }
    
    @RequestMapping("/product/{id}")
    public String getProductById(@PathVariable Integer id, Model model){
    	
    	model.addAttribute("product", productService.getProduct(id));
    	
    	return "product";
    }

	public ProductService getProductService() {
		return productService;
	}

	@Autowired
	public void setProductService(ProductService productService) {
		this.productService = productService;
	}
}
