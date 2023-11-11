package com.shehacks.controller;

import com.shehacks.model.dto.LugarDTO;
import com.shehacks.service.LugarService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageRequest;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import java.net.URI;
import java.util.List;

@RestController
@RequestMapping(value = "/api")
public class LugarController {

	@Autowired
	private LugarService lugarService;

	@GetMapping(value = "/start")
	public ResponseEntity<String> putData(){

		LugarDTO testObj = new LugarDTO(null, "biblioteca", "av paulista", "08:00", "20:00");

		lugarService.insert(testObj);

		return ResponseEntity.ok().body("OK");
	}

	@GetMapping
	public ResponseEntity<List<LugarDTO>> findAll(
			@RequestParam(value = "page", defaultValue = "0") Integer page,
			@RequestParam(value = "size", defaultValue = Integer.MAX_VALUE+"") Integer size) {
		List<LugarDTO> list = lugarService.findAll(PageRequest.of(page, size));
		return ResponseEntity.ok().body(list);
	}

	@GetMapping(value = "/id/{id}")
	public ResponseEntity<LugarDTO> findById(@PathVariable Long id){
		LugarDTO obj = lugarService.findById(id);
		return ResponseEntity.ok().body(obj);
	}

	@GetMapping(value = "/search")
	public ResponseEntity<List<LugarDTO>> findCustomFields(
			@RequestParam(value = "nome", required = false) String nome,
			@RequestParam(value = "endereco", required = false) String endereco,
			@RequestParam(value = "horarioAbre", required = false) String horarioAbre,
			@RequestParam(value = "horarioFecha", required = false) String horarioFecha
	){
		List<LugarDTO> list = lugarService.findCustomFields(nome, endereco, horarioAbre, horarioFecha);
		return ResponseEntity.ok().body(list);
	}

	@PostMapping
	public ResponseEntity<LugarDTO> post(@RequestBody LugarDTO obj){
		LugarDTO c = lugarService.insert(obj);

		URI uri = ServletUriComponentsBuilder.fromCurrentRequest()
				.path("/id/{id}").buildAndExpand(obj.getId()).toUri();

		return ResponseEntity.created(uri).body(c);
	}

	@DeleteMapping(value = "/id/{id}")
	public ResponseEntity<Void> delete(@PathVariable Long id){
		lugarService.delete(id);
		return ResponseEntity.noContent().build();
	}

	@PutMapping(value = "/id/{id}")
	public ResponseEntity<LugarDTO> update (@PathVariable Long id, @RequestBody LugarDTO obj){
		LugarDTO c = lugarService.update(id, obj);
		return ResponseEntity.ok().body(c);
	}
}