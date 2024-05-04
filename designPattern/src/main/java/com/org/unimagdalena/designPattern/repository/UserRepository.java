package com.org.unimagdalena.designPattern.repository;

import com.org.unimagdalena.designPattern.domain.UserEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository extends JpaRepository<UserEntity, Long>{

}
