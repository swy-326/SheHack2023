package com.shehacks.service;

import com.shehacks.exception.ResourceNotFoundException;
import com.shehacks.model.dto.LugarDTO;
import com.shehacks.model.entity.Lugar;
import com.shehacks.model.repository.LugarRepository;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class LugarService {

	@Autowired
	private LugarRepository repository;

	public List<LugarDTO> findAll(Pageable pageable){
		return repository.findAll(pageable).stream().map(LugarDTO::create).collect(Collectors.toList());
	}

	public LugarDTO findById(Long id){
		Optional<Lugar> obj = repository.findById(id);
		return obj.map(LugarDTO::create).orElseThrow(() -> new ResourceNotFoundException(id));
	}

	public List<LugarDTO> findCustomFields(String nome, String endereco, String horarioAbre, String horarioFecha){
		return repository.findCustomFields(nome, endereco, horarioAbre, horarioFecha)
				.stream().map(LugarDTO::create).collect(Collectors.toList());
	}

	public LugarDTO insert(LugarDTO obj) {
		if (obj.getId() != null) throw new IllegalArgumentException("ID nao pode ser atribuido manualmente");
		return LugarDTO.create(repository.save(convertDtoToEntity(obj)));
	}

	public void delete (Long id) {
		try {
			repository.deleteById(id);
		}
		catch (EmptyResultDataAccessException e){
			throw new ResourceNotFoundException(id);
		}
	}

	public LugarDTO update(Long id, LugarDTO obj){
		try {
			Lugar entity = repository.getOne(id);

			ModelMapper modelMapper = new ModelMapper();
			modelMapper.map(obj, entity);
			entity.setId(id); // ignora mudanca de id
			repository.save(entity);

			return LugarDTO.create(entity);
		} catch (RuntimeException e){
			throw new ResourceNotFoundException(id);
		}
	}

	private Lugar convertDtoToEntity(LugarDTO obj){
		ModelMapper modelMapper = new ModelMapper();
		return modelMapper.map(obj, Lugar.class);
	}
}