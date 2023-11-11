package com.shehacks.model.repository;

import com.shehacks.model.entity.Lugar;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface LugarRepository extends JpaRepository <Lugar, Long> {

	@Query(value = "SELECT * FROM tb_lugar " +
			"WHERE (:nome IS NULL OR nome = :nome)  AND " +
			"(:endereco IS NULL OR endereco = :endereco) AND " +
			"(:horarioAbre IS NULL OR horarioAbre = :horarioAbre) AND " +
			"(:horarioFecha IS NULL OR horarioFecha = :horarioFecha)",
			nativeQuery = true)
	List<Lugar> findCustomFields(
			@Param("nome") String nome,
			@Param("endereco") String endereco,
			@Param("horarioAbre") String horarioAbre,
			@Param("horarioFecha") String horarioFecha
	);
}