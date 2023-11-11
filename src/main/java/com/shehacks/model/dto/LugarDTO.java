package com.shehacks.model.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.shehacks.model.entity.Lugar;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.modelmapper.ModelMapper;

import javax.persistence.*;
import java.io.Serializable;

@Data @NoArgsConstructor @AllArgsConstructor
@Entity
@Table(name = "tb_lugar")
public class LugarDTO implements Serializable {

	private static final long serialVersionUID = 1L;

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	@JsonProperty("nome")
	private String nome;
	@JsonProperty("endereco")
	private String endereco;
	@JsonProperty("horarioAbre")
	private String horarioAbre;
	@JsonProperty("horarioFecha")
	private String horarioFecha;

	public static LugarDTO create (Lugar lugar){
		ModelMapper modelMapper = new ModelMapper();
		return modelMapper.map(lugar, LugarDTO.class);
	}
}
